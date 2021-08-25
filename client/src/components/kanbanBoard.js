import React from "react";
import Stage from "./stage";
import { DragDropContext } from "react-beautiful-dnd";
import { stages } from "../data";

const KanbanBoard = () => {
  const renderStage = (items) => {
    var cards = [];
    for (var i = 0; i < items.length; i++) {
      var card = <Stage {...items[i]} />;
      cards.push(card);
    }
    return cards;
  };
  const onDragEnd = (result) => {
    console.log("onDropEnd ==>", result);
  };
  return (
    <main className="inline-flex p-2 h-full overflow-hidden ">
      <DragDropContext onDragEnd={onDragEnd}>
        {renderStage(stages)}
      </DragDropContext>
    </main>
  );
};

export default KanbanBoard;
