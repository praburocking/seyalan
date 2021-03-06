from django.db import connections, router, transaction

SELECT = """
             SELECT last
               FROM {db_table}
              WHERE name = %s
"""


SELECT_ORGSPACE = """
             SELECT org_space
               FROM {db_table}
              WHERE id = %s
"""

POSTGRESQL_UPSERT = """
        INSERT INTO {db_table} (name, last)
             VALUES (%s, %s)
        ON CONFLICT (name)
      DO UPDATE SET last = {db_table}.last + 1
          RETURNING last;
"""

MYSQL_UPSERT = """
        INSERT INTO {db_table} (name, last)
             VALUES (%s, %s)
   ON DUPLICATE KEY
             UPDATE last = {db_table}.last + 1
"""


def get_last_value(
    sequence_name='default',
    *,
    using=None
):
    """
    Return the last value for a given sequence.

    """
    # Inner import because models cannot be imported before their application.
    from .models import Sequence

    if using is None:
        using = router.db_for_read(Sequence)

    connection = connections[using]
    db_table = connection.ops.quote_name(Sequence._meta.db_table)

    with connection.cursor() as cursor:
        cursor.execute(
            SELECT.format(db_table=db_table),
            [sequence_name]
        )
        result = cursor.fetchone()

    return None if result is None else result[0]





def get_space(
    sequence_name='default',
    *,
    using=None
):
    """
    Return the last value for a given sequence.

    """
    print(sequence_name)
    # Inner import because models cannot be imported before their application.
    from .models import Org_Space

    if using is None:
        using = router.db_for_read(Org_Space)

    connection = connections[using]
    db_table = connection.ops.quote_name(Org_Space._meta.db_table)

    with connection.cursor() as cursor:
        cursor.execute(
            SELECT_ORGSPACE.format(db_table=db_table),
            [sequence_name]
        )
        result = cursor.fetchone()
    if result is None:
       return get_next_value(sequence_name,initial_value=int(str(get_next_value('_org_space_'))+"000000000000"))
    return None if result is None else result[0]


def get_range(sequence_name='default',*,using=None):
    space=get_space(sequence_name,using=using)
    return [int(str(space)+"000000000000"),int(str(space)+"999999999999")]


def get_next_value(
    sequence_name='default',
    initial_value=1,
    reset_value=None,
    *,
    nowait=False,
    using=None
):
    """
    Return the next value for a given sequence.

    """
    print("sequence ==>"+str(sequence_name)+" intialValue ==>"+str(initial_value))
    # Inner import because models cannot be imported before their application.
    from .models import Sequence

    if reset_value is not None:
        assert initial_value < reset_value

    if using is None:
        using = router.db_for_write(Sequence)

    connection = connections[using]
    db_table = connection.ops.quote_name(Sequence._meta.db_table)

    if (
        connection.vendor == 'postgresql'
        # connection.features.is_postgresql_9_5 when dropping Django 1.11.
        and getattr(connection, 'pg_version', 0) >= 90500
        and reset_value is None
        and not nowait
    ):

        # PostgreSQL ??? 9.5 supports "upsert".
        # This is about 3x faster as the naive implementation.

        with connection.cursor() as cursor:
            cursor.execute(
                POSTGRESQL_UPSERT.format(db_table=db_table),
                [sequence_name, initial_value]
            )
            result = cursor.fetchone()

        return result[0]

    elif (
        connection.vendor == 'mysql'
        and reset_value is None
        and not nowait
    ):

        # MySQL supports "upsert" but not "returning".
        # This is about 2x faster as the naive implementation.

        with transaction.atomic(using=using, savepoint=False):
            with connection.cursor() as cursor:
                cursor.execute(
                    MYSQL_UPSERT.format(db_table=db_table),
                    [sequence_name, initial_value]
                )
                cursor.execute(
                    SELECT.format(db_table=db_table),
                    [sequence_name]
                )
                result = cursor.fetchone()

        return result[0]

    else:

        # Default, ORM-based implementation for all other cases.

        with transaction.atomic(using=using, savepoint=False):
            sequence, created = (
                Sequence.objects
                        .select_for_update(nowait=nowait)
                        .get_or_create(name=sequence_name,
                                       defaults={'last': initial_value})
            )

            if not created:
                sequence.last += 1
                if reset_value is not None and sequence.last >= reset_value:
                    sequence.last = initial_value
                sequence.save()

            return sequence.last

def create_org_space(using=None,nowait=False):
        from .models import Org_Space
        org_id=get_next_value('_org_id_',initial_value=111111111,reset_value=None,nowait=nowait,using=using)
        org_space=get_next_value('_org_space_',initial_value=1111111)
        org_obj=Org_Space.objects.create(org_space=org_space,id=org_id)
        return org_obj.id


class Sequence:
    """
    Generate a gapless sequence of integer values.

    """
    def __init__(
        self,
        sequence_name='default',
        initial_value=1,
        reset_value=None,
        *,
        using=None
    ):
        if reset_value is not None:
            assert initial_value < reset_value
        if sequence_name=='_org_id_':
            raise Exception('cannot use the given sqeuence name')
        self.sequence_name = sequence_name
        self.initial_value = initial_value
        self.reset_value = reset_value
        self.using = using

    def get_last_value(
        self,
    ):
        """
        Return the last value of the sequence.

        """
        return get_last_value(
            self.sequence_name,
            using=self.using,
        )

    def get_next_value(
        self,
        *,
        nowait=False
    ):
        """
        Return the next value of the sequence.

        """
        return get_next_value(
            self.sequence_name,
            self.initial_value,
            self.reset_value,
            nowait=nowait,
            using=self.using,
        )


    def get_space(self,):
        return get_space(self.sequence_name,using=self.using) 
    def __iter__(self):
        return self

    def __next__(self):
        return self.get_next_value()
    
    def create_org_space(self):
        from .models import Org_Space
        org_space=get_next_value('_org_id_',1111111,None,False,self.using)
        org_obj=Org_Space.objects.create(org_space=org_space)
        return org_obj.id


