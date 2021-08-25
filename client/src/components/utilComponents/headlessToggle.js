import React,{ useState } from 'react'
import { Switch } from '@headlessui/react'

function MyToggle(props) {
 
    const handleEnable=()=>{
        if(props.enabled){
            props.handleDisabled()
        }else{
            props.handleEnabled();
        }
    }
  return (
    <Switch
      checked={props.enabled}
      onChange={handleEnable}
      className={`relative inline-flex items-center h-10 rounded-full w-full focus:outline-none`}
      style={{backgroundColor:'#3b82f6fa'}}
    >  <span className="sr-only color-white">Enable notifications</span>
      <span
        className={`${
          props.enabled ? 'translate-x-full' : 'translate-x-0'
        } inline-block w-1/2 h-9 transform bg-white rounded-full content-center tracking-wider p-1`}
      >    <div>
          {props.enabled?props.enabledText:props.disabledText}
          </div>
          </span>
    </Switch>
  )
}
export default MyToggle;