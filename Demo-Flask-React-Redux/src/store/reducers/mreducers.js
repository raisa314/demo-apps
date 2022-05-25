import { ActionTypes } from "../constant/constant"

const in_state={
    meetings:[ ]
    
}

export const mreducers=(state=in_state,{type, payload})=>
{
  
    switch(type ){

        case ActionTypes.ADD_MEETING:{
            return {...state,
                meetings:payload
            }
            
        }
        case ActionTypes.SEE_DETAIL:{
            return {...state,
               meetings: payload
            }
            
        }

        default : return state
    }
}




