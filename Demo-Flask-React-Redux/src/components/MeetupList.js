import React from "react"
import { useSelector } from "react-redux"

 const MeetupList = (props) =>{


return (
<>
<h3>{props.title}</h3>
   <p> {props.description} </p>
   </>
)
}
export default MeetupList