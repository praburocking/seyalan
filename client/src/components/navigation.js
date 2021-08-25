import React from "react";

const Navigation = (props) => {
  return (
    <>
      {/* <div className="flex inline-flex p-3 lg:hidden">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-list"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"
          />
        </svg>
      </div> */}
      <div
        className={
          "transform " +
          (props.showSideBar
            ? "translate-x-0"
            : "-translate-x-full lg:translate-x-0") +
          " lg:block fixed lg:static inset-y-0 left-0 z-30 bg-gray-100"
        }
      >
        <span className="self-end p-5 rounded-full focus:bg-gray-200 lg:hidden absolute top-0 right-0">
          <button
            onClick={() => props.setSideBar(false)}
            className="focus:outline-none"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-x-lg"
              viewBox="0 0 16 16"
            >
              <path d="M1.293 1.293a1 1 0 0 1 1.414 0L8 6.586l5.293-5.293a1 1 0 1 1 1.414 1.414L9.414 8l5.293 5.293a1 1 0 0 1-1.414 1.414L8 9.414l-5.293 5.293a1 1 0 0 1-1.414-1.414L6.586 8 1.293 2.707a1 1 0 0 1 0-1.414z" />
            </svg>
          </button>
        </span>
        <div className="flex flex-col w-64 bg-gray-100 px-5 h-screen">
          <div className=" py-5">
            <img
              src="assets/images/logo2-removebg-preview.png"
              className="w-15 h-20"
            />
          </div>
          <nav>
            <div className="text-xl uppercase tracking-wider mb-5">
              {" "}
              Issues{" "}
            </div>

            <a href="#">
              <div className="flex item-center justify-between font-bold px-3 py-1 rounded-md bg-gray-300 mx-1">
                {" "}
                <span>All Issues</span> <span>56</span>
              </div>
            </a>
            <a href="#">
              <div className="flex justify-between  px-3 py-1 rounded-md hover:bg-gray-200 mx-1">
                {" "}
                <span>Open Issues</span> <span>10</span>
              </div>
            </a>
            <a href="#">
              <div className="flex justify-between  px-3 py-1 rounded-md hover:bg-gray-200 mx-1">
                {" "}
                <span>My Issues</span>
              </div>
            </a>
            <a href="#">
              <div
                className={
                  "flex justify-between px-3 py-1 rounded-md hover:bg-gray-200 mx-1"
                }
              >
                {" "}
                <span>Closed Issues</span> <span>6</span>
              </div>
            </a>
          </nav>
          <button disableRipple="true">
            <div className="flex bg-red-500 absolute inset-x-0 bottom-0 pt-2 justify-between px-3 text-white hover:bg-red-600 focus:bg-red-800">
              <span>Sign-Out</span>
              <span className="color-white">
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
                  <path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path>
                  <line x1="12" y1="2" x2="12" y2="12"></line>
                </svg>
              </span>
            </div>
          </button>
        </div>
      </div>
    </>
  );
};

export default Navigation;
