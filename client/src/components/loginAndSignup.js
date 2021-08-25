import React, { useState } from "react";
import { Grid, Button } from "@material-ui/core";
import Signin from "./signin";
import SignUp from "./signup";
import Slide from '@material-ui/core/Slide';
import HeadLessToggle from "./utilComponents/headlessToggle";

const LoginAndSignup = (props) => {
  const [isLogin, setLogin] = useState(props.operation==="login");
  return (
    <div className="p-0 m-0 w-screen ">
      <Grid container className="p-0 m-0 ">
        <Grid
          item
          lg={8}
          md={6}
          xs={0}
          className="h-screen p-0 m-0 hidden md:flex bg-blue-500"
        >
          {/* <img src="https://cdn-japantimes.com/wp-content/uploads/2020/06/np_file_16250.jpeg" /> */}
        </Grid>
        <Grid
          item
          lg={4}
          md={6}
          xs={12}
          className="h-screen p-0 m-0 rounded-3xl max-w-2xl rounded-xl"
        >
          <div className="justify-around content-start h-screen">
          <div className="bg-white-500 flex flex-col py-20 lg:px-15 px-5 bg-white-500 sm:px-20  rounded-lg shadow-2xl h-full justify-around">
            <div className="flex flex-row items-center gap-2">
              <img
                className="w-15 h-12"
                src="assets/images/logo.png"
                alt="seyalan logo"
              />
              <span className="text-4xl font-semibold tracking-wider text-gray-800">
                SEYALAN
              </span>
            </div>
            <div>{isLogin ? <Signin /> : <SignUp />}</div>
            <div className="mt-10">
            <HeadLessToggle className="mx-5" enabledText="SIGN-IN" disabledText="SIGN-UP" handleEnabled={()=>setLogin(true)} handleDisabled={()=>setLogin(false)} enabled={isLogin}/>
            </div>
          </div>
         
          </div>
        </Grid>
        
      </Grid>
    </div>
  );
};

export default LoginAndSignup;
