import constants from './constants';
//import dataUtil from '../components/dataUtil'
require('dotenv').config()

export function setCookie(cname, cvalue, exdays) {
    //var d = new Date();
    if(!exdays)
    {
        exdays=30;
    }
    //d.setTime(d.getTime() + (exdays*24*60*60*1000));
    //var expires = "expires="+ d.toUTCString();
    //document.cookie = cname + "=" + cvalue + ";" + expires + ";"+"domain=workmachine.com";
var baseDomain = '.seyalan.com';//+process.env.REACT_APP_SERVER_URL;
console.log("baseDomain ",baseDomain)
var expireAfter = new Date();
 
//setting up  cookie expire date after a week
expireAfter.setTime(expireAfter.getTime() + (exdays*24*60*60*1000));
 
//now setup cookie
document.cookie=cname+"="+cvalue+"; domain=" + baseDomain + "; expires=" + expireAfter + "; path=/";

 
  } // "env:dev": "cross-env NODE_ENV=development REACT_APP_SERVER_URL=workmachine.com REACT_APP_SERVER_PORT=8000 REACT_APP_SERVER_PROTOCOL=http REACT_APP_CLIENT_PORT=3000",
  // "env:prod": "cross-env NODE_ENV=production",

 export  function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    console.log('cookie ==>',decodedCookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) === ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) === 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

  export function deleteCookie(cname, ) {
    document.cookie = cname + "= ; expires =Thu, 01 Jan 1970 00:00:00 GMT ;path=/";
  }

  export  function setTokenCookie (token)
  {
    if(token)
    {
      setCookie("token",token,1);
    }
  }

  export function deleteToken(){
    deleteCookie("token");
  }



  export const setAuthorizationCookies=(userData)=>
  {
    if(userData.user && userData.authtoken && userData.user.username  && userData.user.email)
    {
      setTokenCookie(userData.authtoken)
      setCookie("username",userData.user.username,1);
      setCookie("email",userData.user.email,1);
    }
    else
    {
      throw ("data not found");
    }

  }

  export const deleteAuthorizationCookies=()=>
  {
      deleteToken()
      deleteCookie("username");
      deleteCookie("email");

  }


   export const setAuthorizationHeader=()=>
  {
    const token="Token "+getCookie("token");
    const header={headers:{Authorization:token}};
    return header;

  }
  export const verifyAndGetToken=()=>
  {
    let token=getCookie("token");
    if(!token)
    {
      return undefined;
    }
    else
    {
      return token;
    }

  }

  export const state_to_props=(store)=>
  {
      return ({user:store.user,serverConfig:store.serverConfig,files:store.files,license:store.license})
  }


  export const find_user_cookie_put_to_store=(store)=>
  {
    const user_data={username:getCookie("username"),token:getCookie("token"),id:getCookie("id")};
    store.dispatch({type:"USER_INIT",data:user_data});
  }


  export function extend(obj, src) {
    for (var key in src) {
        if (src.hasOwnProperty(key)) obj[key] = src[key];
    }
    let newObj=obj;
    return newObj;
}