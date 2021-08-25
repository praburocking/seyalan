import axios from'axios'
import {setAuthorizationHeader} from '../util/common_utils'
require('dotenv').config()

console.log("server url",process.env);




//url="https://127.0.0.1:8000/api/v1/"

// let user_url=url+"iam/accounts";
// let login_url=url+"iam/login";
// let logout_url=url+"iam/logout";
// let signup_url=url+"iam/signup"
// let payment_url=url+"payment"
// let forgotPassword_url=url+"iam/forgotpassword"
// let resetPass_url=url+"resetpass"
// let verifyuser_url=url+"iam/verify"
// let uploadfile_url=url+"app/files"
// let getfiles_url=url+"app/files"
// let downloadfiles_url=url+'app/files/download'
// let deletefile_url=url+'app/files'
export const getServerUrl=()=>{
    return window.api_domain;
}
export const signup=async (userData)=>
{
    try {
        let signup_url=getServerUrl()+"/api/iam/signup";
        const response = await axios.post(signup_url, userData);
        return response;
    }
    catch (error) {
        return error.response;
    }
}

// export const signout=async ()=>
// {
//     try {
//         const response = await axios.post(logout_url, { signout: true }, setAuthorizationHeader());
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }


export const login=async (loginData)=>
{   console.log("loginData ",loginData);
    let login_url=getServerUrl()+"/api/iam/login";
    try {
        const response = await axios.post(login_url, loginData);
        return response;
    }
    catch (error) {
        return error.response;
    }
}

export const getUser=async ()=>
{
    try {
        let user_url=getServerUrl()+"/api/iam/accounts";
        const response = await axios.get(user_url, setAuthorizationHeader());
        return response;
    }
    catch (error) {
        return error.response;
    }
}

// export const changePassword=async (data)=>
// {
//     try {
//         const response = await axios.post(user_url+"/passwordchange", data,setAuthorizationHeader());
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }


// export const getUserImage=async()=>
// {
//     try {
//         let config=setAuthorizationHeader()
//         config["responseType"]='blob';
//         console.log("config",config)
//         const response = await axios.get(user_url+"/userimage", config);
//         console.log("userimage response ",response)
//         return response
//     }
//     catch (error) {
//         return error.response;
//     }
// }

// export const addUserImage=async(data)=>
// {
//     try {
//         const response = await axios.post(user_url+"/userimage", data, setAuthorizationHeader());
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }

// export const update_username=async(data)=>{
// try{
//     const response = await axios.patch(user_url, data, setAuthorizationHeader());
//     return response;
// }
// catch (error) {
//     return error.response;
// }
// }


// export const subscribeUser= (data)=>
// {
//     try {
//         const response =  axios.post(payment_url+"/createSubscription",data, setAuthorizationHeader());
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }
// export const geStripeCustomer=async()=>{
//     try{
//         const response=await axios.get(payment_url+"/stripe/customer",setAuthorizationHeader());
//         return  response;
//     }
//     catch(error){
//         return error.response;
//     }
// }

// export const updateStripeCustomer=async(data)=>{
//     try{
//         const response=await axios.patch(payment_url+"/stripe/customer",data,setAuthorizationHeader());
//         return  response;
//     }
//     catch(error){
//         return error.response;
//     }
// }

// export const isUserExist=async (type,data)=>
// {
//     try {
//         const response = await axios.get(signup_url + "/exist?"+type+"=" + encodeURIComponent(data), null);
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }

// export const forgotPassword=async (email)=>
// {
//     try {
//         const response = await axios.post(forgotPassword_url, email);
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }

// export const forgotPasswordVerify=async (key)=>
// {
//     try {
//         const response = await axios.post(forgotPassword_url + "/verifykey?token=" + key);
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }
// export const resetPass=async (key)=>
// {
//     try {
//         const response = await axios.post(resetPass_url, key);
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }
// export const verifyUser=async(token,type,data)=>
// {
//     try {
//         console.log("token ..",token);
//         const response = await axios.post(verifyuser_url+"/"+type+"/"+token,data);
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }

// export const uploadfile=async (data)=>
// {
//     try {
//         const response = await axios.post(uploadfile_url, data,setAuthorizationHeader());
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }

// export const getFiles=async ()=>
// {
//     try {
//         const response = await axios.get(getfiles_url,setAuthorizationHeader());
//         return response;
//     }
//     catch (error) {
//         return error.response;
        
//     }
// }

// export const getDownloadHistory=async (id)=>
// {
//     try {
//         const response = await axios.get(getfiles_url+"/"+id+"/downloadhistory",setAuthorizationHeader());
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }



// export const deleteFile=async (id)=>
// {
//     try {
//         const response = await axios.delete(deletefile_url+"/"+id,setAuthorizationHeader());
//         return response;
//     }
//     catch (error) {
//         return error.response;
//     }
// }

// export const downloadFiles=async (id,key)=>{

//     try{
//     const response=await axios.request({
//         url:downloadfiles_url+"/"+id,
//         method:"POST",
//         headers:setAuthorizationHeader().headers,
//         data: {
//             private_key:key
//           },
//         responseType: 'blob'
//         })
//     return response
//     }
//     catch (error) {
//         return error.response;
//     }
// }