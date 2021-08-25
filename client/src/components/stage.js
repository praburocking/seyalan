import React from "react";
import Card from "./card";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";
import { kanbanData } from "../data";

const Stage = (props) => {
  const renderCards = (items) => {
    var cards = [];
    for (var i = 0; i < items.length; i++) {
      var card = <Card {...items[i]} index={i} />;
      cards.push(card);
    }
    return cards;
  };
  return (
    <div className="flex flex-row w-80">
      <div
        className={
          "h-full flex flex-col flex-shrink-0  py-1 bg-" +
          props.color +
          "-100  mx-1 rounded-md"
        }
      >
        <div className="flex flex-shrink-0 p-2 justify-between align-items-center">
          <span className="inline-flex">
            <h3 className="text-gray-600">{props.title}</h3>
            <span className="hidden hover:block">
              <svg
                className="h-4 w-4"
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <polygon points="16 3 21 8 8 21 3 21 3 16 16 3"></polygon>
              </svg>
            </span>
          </span>
          <span className="text-gray-600">
            <button
              className={
                "rounded-full hover:bg-" +
                props.color +
                "-200 focus:bg-" +
                props.color +
                "-300 focus:outline-none"
              }
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <circle cx="12" cy="12" r="1"></circle>
                <circle cx="12" cy="5" r="1"></circle>
                <circle cx="12" cy="19" r="1"></circle>
              </svg>
            </button>
          </span>
        </div>
        <div className=" flex-1 min-h-0 overflow-y-auto">
          <Droppable droppableId={props.id}>
            {(provided) => (
              <ul {...provided.droppableProps} ref={provided.innerRef}>
                {renderCards(kanbanData[props.id])}
                {provided.placeholder}
              </ul>
            )}
          </Droppable>
        </div>
      </div>
    </div>
  );
};
export default Stage;
