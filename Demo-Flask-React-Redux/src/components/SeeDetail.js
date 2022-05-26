import { useEffect,useState } from "react";
import { useSelector } from "react-redux";
import { useDispatch } from "react-redux";

export const SeeDetail = (props) => {
    let meetings = useSelector((state) => state.allmeeting.meetings);
       const [toggle_details,setToggle_details] = useState(false);
   
     const onDetailsBtnClick = () =>{
       setToggle_details(!toggle_details);
       console.log(toggle_details);
   }
   console.log(meetings)
   return( 
   
   <div className="meetup-actions">
   <button className="btn" onClick={()=>onDetailsBtnClick()}>More Details</button>

   {toggle_details?
   <div>
   <article>
   {/* <img src="" alt=""> */}
   
   <section id="details">
   <h3>{meetings.Title[props.count]} </h3>

   
   <section id="location">
   <h2>Meetup Location</h2>
   <address>This meetup takes place in <span>{meetings.description[props.count]}</span> </address>
   </section>
   
   <footer>
       <p>Need more details? Please <a href="">contact the organizer</a> (but don't spam us)</p>
   </footer>
   </section>
   
   <section id="registration">
            <h2>Join US!</h2>FORM
  </section>
   
   </article>
   </div>
   :""}
   </div>
   )}