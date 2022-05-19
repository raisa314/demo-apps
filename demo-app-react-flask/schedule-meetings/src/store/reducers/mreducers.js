import { ActionTypes } from "../constant/constant"

const in_state={
    meetings:[
       {
         title:" comp",
        description:"lets change",
       }
    ]
}

export const mreducers=(state=in_state,{type, payload})=>
{
  
    switch(type ){

        case ActionTypes.ADD_MEETING:{
            return state
            
        }
        case ActionTypes.SEE_DETAIL:{
            return state
            
        }

        default : return state
    }
}




