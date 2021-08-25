import React,{useState} from 'react';
import { withRouter } from "react-router-dom";
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

const useStyles = makeStyles({
    root: {
      flexGrow: 1,
    },
  });
  
const SettingListView=(props)=>{
    const classes = useStyles();
  const [value, setValue] = React.useState(0);
    const handleBack=()=>{
        props.history.push('/home');
      } 
      const handleChange = (event, newValue) => {
        setValue(newValue);
      };
    return(
        <div className="w-screen h-screen flex flex-col">
        <div className="flex items-center">
        <div>
          <button onClick={()=>handleBack()}>
        <img className="h-8" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAAr0lEQVRoge3ZMaoCQRBF0at7cND9r8RIFE3+D1yOBiYiJlX4CpF74rnNvE4bJH2LBbgA+3ATtQD/wA04BpuoDfDH44euwDbURDmi0EQ5otBEOaLQRDmi0EQ5otBEOaLQRDmi0EQ5otBEOaLQfMS68O2qcX6niXi94V2oGeGYRjPCMY1mhGMazQjHNJoRjmk0IxzTaEY4ptGMcEyjGfFTY56fmk/BZsQCnIFDuJH0xh3rX+MbPE18WAAAAABJRU5ErkJggg=="/>
        </button>
        </div>
      <div className="container text-center text-3xl tracking-widest font-semibold py-2 md:py-5">Settings</div>
      </div >
        <div className="h-full w-full"> 


        <div className="grid grid-cols-4 gap-2 h-full w-full">
            <div className="flex bg-red-100 mb-5 rounded-xl ml-5 flex-col">
                <button className="h-16 bg-red-300 rounded-xl mb-1">User</button>
                <button className="h-16 bg-red-200 rounded-xl mb-1">Organization</button>
                <button className="h-16 bg-red-200 rounded-xl mb-1">pipeline</button>
               
            </div>
            <div className="flex flex-col items-center w-full col-span-3 bg-red-100 mb-5 rounded-xl mr-5" >
            {/* <Paper className="flex-grow-1 bg-red-100">
                    <Tabs
                        value={value}
                        onChange={handleChange}
                        indicatorColor="primary"
                        textColor="primary"
                        centered
                    >
                        <Tab label="Item One" className="bg-red-100"/>
                        <Tab label="Item Two" />
                        <Tab label="Item Three" />
                    </Tabs>
                    </Paper> */}
            </div>
        </div>
        </div>
       
        </div>

    );
}

export default withRouter(SettingListView) //className="flex col-span-3 bg-red-100 mb-5 rounded-xl mr-5"