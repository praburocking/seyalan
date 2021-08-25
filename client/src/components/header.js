import React, { useState } from "react";
import KanbanBoard from "./kanbanBoard";
import CalendarView from "./calendar";
import { withRouter } from "react-router-dom";

const Header = (props) => {
  const [getView, setView] = useState("calendar");

const handleSettings=()=>{
props.history.push('/settings')
}

  return (
    <div className=" flex flex-col flex-1 min-w-0 overflow-hidden">
      <div className="bg-white-400 sm:border-b-2  h-30 min-w-0">
        <header className="pl-3 ">
          <div className=" flex justify-between items-center border-b py-1">
            <div className="my-3 flex flex-1 px-1 items-center min-w-0s">
              {/*side bar button*/}
              <span className="inline lg:hidden mr-5">
                <button onClick={() => props.setSideBar(!props.showSideBar)}>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-15 w-15"
                    width="30"
                    height="30"
                    fill="currentColor"
                    class="bi bi-list"
                    viewBox="0 0 16 16"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"
                    />
                  </svg>
                </button>
              </span>
              <div className=" flex-shrink-1  relative ">
                <button >
                <span className="absolute  inset-y-0 left-0 flex items-center pl-1">
                  <svg
                    className="h-5 w-5"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 64 64"
                  >
                    <g data-name="Layer 2">
                      <path
                        d="M63.22 59.45L47.3 43.53a26.7 26.7 0 10-3.77 3.77l15.92 15.92a2.67 2.67 0 003.77-3.77zM26.67 48A21.34 21.34 0 1148 26.67 21.36 21.36 0 0126.67 48z"
                        fill="#35353d"
                        data-name="Layer 1"
                      />
                    </g>
                  </svg>
                  
                </span>
                </button>
                <input
                  placeholder="Search"
                  className=" pl-8 py-2 outline-none border border-gray-400 rounded-md leading-tight"
                ></input>
              </div>
            </div>
            <div div="flex item-center justify-center h-30 flex-shrink-0">
              <button className=" focus:outline-none h-7 w-7 hover:bg-gray-300 " onClick={()=>handleSettings()}>
              <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAAuElEQVRoge3Y0QqDMAwF0DvZx038/x+w/Y/uZUNlChGT3kXugb70IW0MpEFARLxMACqA9lkFwEi90UkFy+W/a44+9OEYq3U448cQGbyH587e0Zf0cjX+pqLpK6AE2NSF2DwTqDt7xTF+uBHb13gG8KLeSG5KU+taaI8+4PpepH8HGNOolalS6SugBNjUhdgYCWhqlWw0PUay9F7K3war9O+A5zTaa4rVNPpX0iegLsRmSUDTo4jEeQPGvDzTx5BsMwAAAABJRU5ErkJggg=="/>
              </button>
              <button className="focus:outline-none mx-2">
                <img
                  className="rounded-full w-9 h-9 object-cover outline-none"
                  src="assets/images/pp1.jpg"
                />
              </button>
            </div>
          </div>
          <div className="py-2 pr-2 flex justify-between">
            <div className="flex flex-row justify-between sm:justify-none">
              <h2 className="text-2xl  font-bold text-gray-700 pr-4">
                ALL ITEMS
              </h2>
              <div className="flex pl-3">
                <span className="  -ml-2">
                  <img
                    src="assets/images/pp1.jpg"
                    className="w-7 h-7 rounded-full border-white border-2 "
                  />
                </span>
                <span className="  -ml-2">
                  <img
                    src="assets/images/pp2.jpg"
                    className="w-7 h-7 rounded-full border-2 border-white"
                  />
                </span>
                <span className=" -ml-2">
                  <img
                    src="assets/images/pp3.jpg"
                    className="w-7 h-7 rounded-full  border-2 border-white"
                  />
                </span>
              </div>
            </div>
            <div className="items-center  sm:flex hidden">
              <div className="bg-gray-300 p-1 rounded inline ">
                {/*calendar view */}
                <button
                  className={
                    getView == "calendar"
                      ? "bg-white p-1 rounded-md outline-none focus:outline-none"
                      : "p-1 rounded-md outline-none focus:outline-none"
                  }
                  onClick={() => setView("calendar")}
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    fill="currentColor"
                    class="bi bi-calendar3"
                    viewBox="0 0 16 16"
                  >
                    <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857V3.857z" />
                    <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
                  </svg>
                </button>
                {/*kanbanview view */}
                <button
                  className={
                    getView == "kanban"
                      ? "bg-white p-1 rounded-md focus:outline-none"
                      : " p-1 rounded-md focus:outline-none"
                  }
                  onClick={() => setView("kanban")}
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    fill="currentColor"
                    class="bi bi-layout-three-columns"
                    viewBox="0 0 16 16"
                  >
                    <path d="M0 1.5A1.5 1.5 0 0 1 1.5 0h13A1.5 1.5 0 0 1 16 1.5v13a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 14.5v-13zM1.5 1a.5.5 0 0 0-.5.5v13a.5.5 0 0 0 .5.5H5V1H1.5zM10 15V1H6v14h4zm1 0h3.5a.5.5 0 0 0 .5-.5v-13a.5.5 0 0 0-.5-.5H11v14z" />
                  </svg>
                </button>
              </div>
              <div>
                <button className="px-3 py-2 bg-gray-800 hover:bg-gray-600 focus:bg-gray-500 text-white focus:outline-none mx-2 rounded-md ">
                  <div className="flex">
                    <span>
                      {" "}
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
                        <line x1="12" y1="5" x2="12" y2="19"></line>
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                      </svg>
                    </span>
                    <span>New Item</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </header>
        <div className="mx-1 text-gray-800">
          <div className="bg-gray-300 p-1 rounded flex flex-1 sm:hidden">
            {/*calendar view mobile */}
            <button
              className={
                getView == "calendar"
                  ? "bg-white p-1 rounded-md outline-none focus:outline-none flex flex-grow items-center justify-around"
                  : "p-1 rounded-md outline-none focus:outline-none flex flex-grow items-center justify-around"
              }
              onClick={() => setView("calendar")}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="inline"
                width="24"
                height="24"
                fill="currentColor"
                class="bi bi-calendar3"
                viewBox="0 0 16 16"
              >
                <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857V3.857z" />
                <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
              </svg>
              <span> Calendar View</span>
            </button>
            <button
              className={
                getView == "kanban"
                  ? "bg-white p-1 rounded-md focus:outline-none flex flex-grow items-center justify-around"
                  : " p-1 rounded-md focus:outline-none flex flex-grow items-center justify-around"
              }
              onClick={() => setView("kanban")}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                fill="currentColor"
                class="bi bi-layout-three-columns"
                viewBox="0 0 16 16"
              >
                <path d="M0 1.5A1.5 1.5 0 0 1 1.5 0h13A1.5 1.5 0 0 1 16 1.5v13a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 14.5v-13zM1.5 1a.5.5 0 0 0-.5.5v13a.5.5 0 0 0 .5.5H5V1H1.5zM10 15V1H6v14h4zm1 0h3.5a.5.5 0 0 0 .5-.5v-13a.5.5 0 0 0-.5-.5H11v14z" />
              </svg>
              Kanban View
            </button>
          </div>
        </div>
      </div>
      <div className="flex-1 overflow-auto">
        {getView == "calendar" && <CalendarView />}
        {getView == "kanban" && <KanbanBoard />}
      </div>
    </div>
  );
};

export default withRouter(Header);
