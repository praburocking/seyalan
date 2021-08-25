import React,{useState} from "react";
import { TextField, Button } from "@material-ui/core";
import {user as userRepo,auth as authRepo,org as orgRepo} from "../store/atoms"
import { useRecoilState, useRecoilValue } from "recoil";
import {login} from '../services/connectToServer'
import {setTokenCookie,setCookie} from '../util/common_utils'
import { Transition } from '@headlessui/react'
import { green } from '@material-ui/core/colors';
import {
  fade,
  ThemeProvider,
  withStyles,
  makeStyles,
  createMuiTheme,
} from '@material-ui/core/styles';
import {
  useHistory
} from "react-router-dom";
import Paper from '@material-ui/core/Paper';
import  CustomSnackbar from './utilComponents/snackbar'
import Alert from "./utilComponents/alert"


const theme = createMuiTheme({
  palette: {
    primary: {main:"#3b82f6fa",light:"#3b82f6fa",dark:"#3b82f6fa"},
  },
});

const Signin = () => {
  const [userData,setUserData]=useRecoilState(userRepo);
  const [authData,setAthuData]=useRecoilState(authRepo);
  const [orgData,setOrgData]=useRecoilState(orgRepo);
  let history = useHistory();
  const [email,setEmail]=useState('');
  const [password,setPassword]=useState('');
  const [alertData,setAlertData]=useState({show:true,message:"this is teset",color:"blue"});

  const onAlertClose=()=>{  
    console.log("test")
    setAlertData({...{alertData},show:false});
  }
  

  const Handlelogin=async (email,password)=>{
    const reqObj={"email":email,"password":password};
    const response =await login(reqObj);

    if(response.status===200){
      setUserData(response.data.user)
      setTokenCookie(response.data.authtoken);
      setAthuData(response.data.authtoken);
      setOrgData(response.data.org);
      setCookie("domain",response.data.org.domain,1);
      window.location="http://"+response.data.org.domain+":3000"

    }
    else{
      
     setAlertData({...{alertData},color:"red",message:response.data&&response.data.detail?response.data.detail:"unknow error",show:true});
    }
  }

  return (
   <>
    <ThemeProvider theme={theme}>
      <div className="pt-5 text-lg tracking-widest text-3xl mb-5">
        <span className="font-bold "> Login </span>to Contine
      </div>
       < CustomSnackbar type="error" message="invalid credentials" onclose={onAlertClose}/> 
      {console.log("alert data ",alertData)}
       <Alert show={alertData.show} message={alertData.message} color={alertData.color} onClose={()=>onAlertClose()}/>
       
      <div className="w-100 h-250 mt-5">
        <div className="flex flex-col h-100">
          <TextField
            id="standard-basic"
            fullWidth
            label="email"
            variant="outlined"
            value={email}
            onChange={(event)=>setEmail(event.target.value)}
          />
          <br />
          <TextField
            id="standard-basic"
            label="password"
            variant="outlined"
            fullWidth
            type="password"
            value={password}
            onChange={(event)=>setPassword(event.target.value)}
          />
          <br />
          <Button variant="contained" className="focus:outline-none rounded-full" color="primary" size="large" onClick={()=>Handlelogin(email,password)}>
            Login
          </Button>
        </div>
      </div>
      </ThemeProvider>
   </>
  );
};

export default Signin;
