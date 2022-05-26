import { useEffect,useState } from "react";
import "./base.css";
import "./main.css";
import "./meetup-details.css";
import "./add_meeting.css";
import axios from "axios"
import { useSelector } from "react-redux";
import { useDispatch } from "react-redux";
import { setMeeting } from "./store/actions/mactions";
import { SeeDetail } from "./components/SeeDetail";

var count=0;
function App() { 
    const handleSubmit = async(event) => {
        event.preventDefault();
        window.location = "http://localhost:3000/";
        console.log("handleSubmit Runs");
        var title=event.target.title.value;
        var description= event.target.description.value;
        const response= await axios
        .post('/add_meetups',
        {title:title,
        description:description}
        )
        .catch(error => console.log(error))

      };

    //const [toggle_details,setToggle_details] = useState(false);
    const [toggle_add,setToggle_add] = useState(false);
    const dispatch= useDispatch();

    // const onDetailsBtnClick = (count) =>{
    //     setToggle_details(!toggle_details);
    //     //console.log(toggle_details);
    // }

    const onAddBtnClick = () =>{
        setToggle_add(!toggle_add);
        //console.log(toggle_add);
    }

    const fetchmeeting= async()=>{
        const response=await axios
        .get('http://localhost:5000/')
        .catch(error => console.log(error))
        dispatch(setMeeting(response.data))
    } 

  useEffect(()=>{
  fetchmeeting();
  },[]);
  
  const meet = useSelector((state) => state.allmeeting.meetings);
  return ( 
      <>
        <header id="main-header">
          <nav><a href="" id="main-logo">Flask meetups</a></nav>
          <p>Find the one that best suits your needs</p>
        </header>
        
        <section>
            <div className="meetup-actions">
                <button className="btn" onClick={()=>onAddBtnClick()}>Add Meetup</button>
            </div>
            
            {toggle_add?
                <div className="column is-4 is-offset-4 form-group">
                <h3 className="title">Add Meeting</h3>
                <div className="box">
                    <form method="POST" onSubmit={handleSubmit}>
                        <div className="field">
                        <div className="control">
                                <input className="input is-large" type="text" name="title" placeholder="title" autoFocus=""/>
                            </div>
                        </div>
            
                        <div className="field">
                            <div className="control">
                                <input className="input is-large" type="text" name="description" placeholder="description" autoFocus=""/>
                            </div>
                        </div>
            
                        <input onclick="window.location.href = 'http://localhost:3000';" type="submit" value="Submit" />
                    </form>
                </div>
            </div>
                :""}
        </section>

        <section> <h2>Upcoming meetups</h2> </section>
          {(Object.keys(meet).length !==0) && 
        <> 
        {/* {count=-1} */}
        {meet.Title.map((element,count) => { 
            //console.log("element", element)
            //count++
    return (<>
        <section>
        <ol key={element}>
        <li className="meetup-item" key={element}>
        <article>
        <div className="meetup-summary">
            <div className="meetup-image">
                <img src="https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" alt=""/>
            </div>
            
            <div className="meetup-details">
                <h3>{meet.Title[count]}</h3> 
                <p>{meet.description[count]}</p>
            </div>
        </div>
        
        <SeeDetail count={count}/>
        {/* <div className="meetup-actions">
            <button className="btn" onClick={()=>onDetailsBtnClick(count)}>More Details</button>
        </div>
        {toggle_details?
        <div>
        <article>
        
        <section id="location">
            <h2>Meetup Location</h2>
            <h4>This meetup takes place in {meet.Title[count]} </h4>
        </section>

        <section id="details">
            <h2>What's this Meetup is about?</h2>
            <p>{meet.Title[count]}{console.log("title:", count)}</p>
            <p>{meet.description[count]}</p>
            <footer>
                <p>Need more details? Please <a href="">contact the organizer</a> (but don't spam us)</p>
            </footer>
        </section>

        <section id="registration">
            <h2>Join US!</h2>
            FORM
        </section>
        </article>
        </div>
    :""} */}
            </article>
            </li>
            </ol>
        </section>
        
    </>) 
})} </>
      
}</>
  );
}

export default App;
