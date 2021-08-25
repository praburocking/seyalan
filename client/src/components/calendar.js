import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import withDragAndDrop from "react-big-calendar/lib/addons/dragAndDrop";
import React, { useState } from "react";

import "react-big-calendar/lib/addons/dragAndDrop/styles.css";
import "react-big-calendar/lib/css/react-big-calendar.css";

const localizer = momentLocalizer(moment);
const DnDCalendar = withDragAndDrop(Calendar);
const CalendarView = (props) => {
  const [events, setEvent] = useState([
    {
      start: moment().toDate(),
      end: moment().add(1, "days").toDate(),
      title: "Some title"
    }
  ]);
  const onEventResize = (data) => {
    // const { start, end } = data;
    // setEvent() => {
    //   events[0].start = start;
    //   events[0].end = end;
    //   return { events: [...events] };
    // };
  };

  const onEventDrop = (data) => {
    console.log(data);
  };

  return (
    <div className="App">
      <DnDCalendar
        defaultDate={moment().toDate()}
        defaultView="month"
        events={events}
        localizer={localizer}
        onEventDrop={onEventDrop}
        onEventResize={onEventResize}
        resizable
        style={{ height: "100vh" }}
      />
    </div>
  );
};

export default CalendarView;
