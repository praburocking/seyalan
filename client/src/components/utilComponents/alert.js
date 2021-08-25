import React from "react";

 const Alert=(props)=>{
     console.log(props)
    return(
        <>
        {props.show && 
        <div className="w-full">
        <div className={"py-3 px-5 mb-4 bg-"+props.color+"-100 text-"+props.color+"-900 text-sm rounded-md border border-"+props.color+"-200 flex items-center justify-between"} role="alert">
           <div className="flex"> <div class="w-4 mr-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                </svg>
            </div>
            <span>{props.message}</span>
            </div>
            <button className="w-4" type="button" data-dismiss="alert" aria-label="Close" onClick={props.onClose}>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
        </div>
        </div>
        }
        </>
    );
}
export default Alert;