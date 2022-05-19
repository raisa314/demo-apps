import { ActionTypes } from "../constant/constant";

export const setMeeting=(metting)=>{
    return{
        type: ActionTypes.ADD_MEETING,
        payload: metting,
    }
}


export const setDetail=(meeting)=>{
    return{
        type: ActionTypes.SEE_DETAIL,
        payload:meeting,
    }
}



