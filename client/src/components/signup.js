import React,{useState} from "react";
import { TextField, Button } from "@material-ui/core";
import {user as userRepo,auth as authRepo,org as orgRepo} from "../store/atoms"
import { useRecoilState, useRecoilValue } from "recoil";
import {signup} from '../services/connectToServer';
import {setTokenCookie,setCookie} from '../util/common_utils'
import {
  fade,
  ThemeProvider,
  withStyles,
  makeStyles,
  createMuiTheme,
} from '@material-ui/core/styles';

const theme = createMuiTheme({
  palette: {
    primary: {main:"#3b82f6fa",light:"#3b82f6fa",dark:"#3b82f6fa"},
  },
});
const SignUp = () => {
  const [isOrgPage,setOrgPage] =useState(false);
  const [orgName,setOrgName]=useState("");
  const [userName,setUserName]=useState("");
  const [password,setPassword]=useState("");
  const [domain,setDomain]=useState("");
  const [email,setEmail]=useState("");
  const [userData,setUserData]=useRecoilState(userRepo);
  const [authData,setAthuData]=useRecoilState(authRepo);
  const [orgData,setOrgData]=useRecoilState(orgRepo);
  const [alertData,setAlertData]=useState({show:false,message:"this is teset",color:"blue"});

const handleCreateAccount=async()=>{
  const user={username:userName,email:email,password:password}
  const org={name:orgName,domain:domain}
  const request={user:user,org:org}
  const response=await signup(request);

  if(response.status===201){
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
      {!isOrgPage && <>
      <div className="pt-5 text-lg tracking-widest text-3xl">
        Create Account
      </div>

      <div className="w-100 h-250 mt-10">
        <div className="flex flex-col h-100">
          <TextField
            id="standard-basic"
            label="Name"
            variant="outlined"
            fullWidth
            value={userName}
            onChange={(event)=>setUserName(event.target.value)}
          />
          <br />
          <TextField id="email" fullWidth label="Email" variant="outlined" 
           value={email}
           onChange={(event)=>setEmail(event.target.value)}/>
          <br />
          <TextField
            id="password"
            label="password"
            variant="outlined"
            fullWidth
            value={password}
            onChange={(event)=>setPassword(event.target.value)}
            type="password"
          />
          <br />
          <Button variant="contained" color="primary" size="large" onClick={()=>setOrgPage(true)}>
            Create Account
          </Button>
        </div>
      </div>
      </>
      }
      {isOrgPage && <>
        <div className="pt-5 text-lg tracking-widest text-3xl">
      Add Org Details
      </div>

      <div className="w-100 h-250 mt-10">
        <div className="flex flex-col h-100">
        
          <TextField id="Org Name" fullWidth label="Org Name" variant="outlined"  value={orgName}
            onChange={(event)=>setOrgName(event.target.value)}/>
          <br />
          <TextField
            id="standard-basic"
            label="domain"
            variant="outlined"
            fullWidth
            value={domain}
            onChange={(event)=>setDomain(event.target.value)}
          />
          <br />
          <Button variant="contained" color="primary" size="large" onClick={()=>handleCreateAccount()}>
            Create Account
          </Button>
        </div>
      </div>

      </>}
      </ThemeProvider>
    </>
  );
};

export default SignUp;
