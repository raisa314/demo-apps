import { combineReducers } from "redux";
// import { mreducers } from "./mreducers"
import { mreducers } from "./mreducers"


const reducers=combineReducers({
    allmeeting: mreducers,
})


export default reducers



