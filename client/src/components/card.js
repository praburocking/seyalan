import { getThemeProps } from "@material-ui/styles";
import Rect from "react";
import { Draggable } from "react-beautiful-dnd";

const Card = (props) => {
  return (
    <Draggable
      key={props.id.toString()}
      draggableId={props.id.toString()}
      index={props.index}
    >
      {(provided) => (
        <li
          ref={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
          className="focus:outline-none"
        >
          <span
            href="#"
            className=" block px-2 py-5 bg-white shadow-md m-2 rounded-md hover:shadow-lg"
          >
            <div className="flex justify-between">
              <p className="text-sm font-medium text-gray-800 leading-snug">
                {props.title}
              </p>
              {props.userImage && (
                <span>
                  <img className="rounded-full w-6 h-6" src={props.userImage} />
                </span>
              )}
            </div>
            <div className="flex justify-between my-2 items-center">
              <div className="text-gray-500 text-sm">{props.date}</div>
              <div>
                {props.badge && (
                  <span
                    className={
                      "px-1 bg-" +
                      props.badgeColor +
                      "-200 inline-flex justify-between rounded items-center py-1 leading-tight"
                    }
                  >
                    <svg
                      className={"w-3 h-3 text-" + props.badgeColor + "-500"}
                      viewBox="0 0 8 8"
                      fill="currentColor"
                    >
                      <circle cx="4" cy="4" r="3" />
                    </svg>
                    <span className="ml-1 text-sm leading-wide">
                      {props.badge}
                    </span>
                  </span>
                )}
              </div>
            </div>
          </span>
        </li>
      )}
    </Draggable>
  );
};

export default Card;
