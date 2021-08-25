import React, { useState } from "react";
import KanbanBoard from "./kanbanBoard";
import CalendarView from "./calendar";
import { withRouter } from "react-router-dom";
import PersonAddIcon from '@material-ui/icons/PersonAdd';
import BusinessIcon from '@material-ui/icons/Business';

const SettingsPage = (props) => {
  const [getView, setView] = useState("calendar");

const handleSettings=(item)=>{
  console.log('pushing to','/settings/'+item);
props.history.push('/settings/'+item);

}

const handleBack=()=>{
  props.history.push('/home');
}
  return (
    <div className=" flex flex-col flex-1 min-w-0 overflow-hidden h-screen bg-gray-100">
      <div className="flex items-center">
        <div>
          <button onClick={()=>handleBack()}>
        <img className="h-8" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAAr0lEQVRoge3ZMaoCQRBF0at7cND9r8RIFE3+D1yOBiYiJlX4CpF74rnNvE4bJH2LBbgA+3ATtQD/wA04BpuoDfDH44euwDbURDmi0EQ5otBEOaLQRDmi0EQ5otBEOaLQRDmi0EQ5otBEOaLQfMS68O2qcX6niXi94V2oGeGYRjPCMY1mhGMazQjHNJoRjmk0IxzTaEY4ptGMcEyjGfFTY56fmk/BZsQCnIFDuJH0xh3rX+MbPE18WAAAAABJRU5ErkJggg=="/>
        </button>
        </div>
      <div className="container text-center text-3xl tracking-widest font-semibold py-2 md:py-5">Settings</div>
      </div >
      <div className="grid grid-cols-3 gap-2 h-full w-full m-5">
      <button onClick={()=>handleSettings('user')} className="bg-red-100 h-full w-full  flex flex-1 justify-center items-center rounded-xl"><div class="flex flex-col items-center"><PersonAddIcon style={{fontSize:60}}/>
      <div>Users</div>
      </div></button>
      <div className="bg-red-100 h-full w-full  flex flex-1 justify-center items-center rounded-xl"><div class="flex flex-col items-center">
      <BusinessIcon style={{fontSize:60}}/>
      <div>Company Info </div>
        </div></div>

      <div className="bg-red-100 h-full w-full  flex flex-1 justify-center items-center rounded-xl"><div class="place-self-center">1</div></div>

      <div className="bg-red-100 h-full w-full  flex flex-1 justify-center items-center rounded-xl"><div class="place-self-center">1</div></div>

      <div class="bg-red-100 h-full w-full  flex flex-1 justify-center items-center rounded-xl"><div class="place-self-center">1</div></div>


</div>
    </div>
  );
};

export default withRouter(SettingsPage);
