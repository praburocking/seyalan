import {createStore,combineReducers} from 'redux'
import userReducer from './user'
import thunk from 'redux-thunk'

import { applyMiddleware } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension'


const combine_reducer=combineReducers({
    user:userReducer,
})


const store=createStore(combine_reducer,composeWithDevTools(applyMiddleware(thunk)));
export default store; 