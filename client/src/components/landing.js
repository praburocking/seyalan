import React,{useEffect} from "react";
import { withRouter } from "react-router-dom";


const LandingPage=(props)=>{

    return(
        <div className="w-screen items-center mx-auto">
            {/* header-starts */}
            <header>
                <nav className="flex items-center mx-4 px-4 mt-4 ">
                    <div className="flex">
                    <div><img src="assets/images/logo.png" className="w-9 h-5 m-2"></img></div>
<div className="hidden sm:block tracking-widest text-gray-800 text-xl font-semibold">SEYALAN</div>
</div>
<ul className=" hidden sm:flex flex-1 justify-end items-center uppercase gap-12 text-blue-500 text-xs">
    <li className="cursor-pointer">Features</li>
    <li className="cursor-pointer">Pricing</li>
    <li className="cursor-pointer">contacts</li>
    <button className="bg-red-500 hover:bg-red-600 focus:bg-red-700 uppercase py-2 px-4 rounded-md text-white focus:outline-none">Log-in</button>
    <button className="bg-red-500 hover:bg-red-600 focus:bg-red-700 uppercase py-2 px-4 rounded-md text-white focus:outline-none">sign-up</button>

</ul>
<div className="flex flex-1 sm:hidden justify-end text-lg"><i class="fas fa-bars"></i></div>
                </nav>

            </header>
            {/* header-ends */}
<section className=" relative container bg-gray-100">
    {/* hero --1 */}
<div className="flex flex-col-reverse lg:flex-row items-center gap-12 mt-14 lg:mt-28 px-20   z-10  rounded-lg py-10 lg:mx-20 mx-0">
    {/* left text */}
    <div className="flex flex-col items-center lg:items-start gap-5 ">
        <h1 className="lg:text-3xl tracking-wider text-gray-800 text-2xl text-bold">
            Organize your work like a pro!
        </h1>
        <div className="flex flex-col gap-2">
        <p>
            SEYALAN helps you to Organize your work in single place with our flagship pipeline based organizer, consolidate your work and increase your productivity.
        </p>
        <div className="flex gap-14 justify-center lg:justify-start">
            <button className="rounded bg-blue-500 text-white px-4 py-2 hover:bg-blue-600 focus:bg-blue-700" type="button" onClick={()=>props.history.push("/signup")}>Sign up</button>
            <button className="rounded bg-gray-200 px-4 py-2 hover:bg-gray-300 focus:bg-gray-400" type="button" onClick={()=>props.history.push("/login")}>Sign In</button>
        </div>
        </div>
    </div>
    {/* left text end */}
    {/* right image */}
<div className="flex justify-center z-20">
    <img className="w-5/6 h-full rounded-lg"src="assets/images/kanbanview.png" alt="kanbanview image"/>
    
</div>

    {/* right image end     */}
</div>
<div className="absolute overflow-hidden h-3/4 w-1/2 rounded-l-full bg-blue-500 top-64 left-3/4  lg:block hidden z-0"/>




</section>
            {/* hero starts */}
           
        </div>
    )
}

export default withRouter(LandingPage);
