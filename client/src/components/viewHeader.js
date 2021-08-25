import React from "react";
const viewHeader = () => {
  return (
    <div className="py-2 flex justify-between">
      <div className="flex">
        <h2 className="text-2xl  font-bold text-gray-700 pr-4">ALL ITEMS</h2>
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
      <div className="flex">
        <div className="flex bg-gray-300">
          <button>
            <div className="w-7 h-7 p-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#807c7c"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
              </svg>
            </div>
          </button>
          <button>
            <div className="w-7 h-7 p-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#807c7c"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <rect x="3" y="3" width="7" height="7"></rect>
                <rect x="14" y="3" width="7" height="7"></rect>
                <rect x="14" y="14" width="7" height="7"></rect>
                <rect x="3" y="14" width="7" height="7"></rect>
              </svg>
            </div>
          </button>
        </div>
      </div>
    </div>
  );
};

export default viewHeader;
