import "./meetup-details.css"
import { useEffect,useState } from "react";
import { useLocation, useParams } from "react-router-dom";

const Meetupid = (props) => {
    const [articles, setArticles] = useState([]);
    // const cors = require('cors');
    // Meetupid.use(cors())
    useEffect(()=>{
       fetch(`http://localhost:5000/meetup/${id}`,{
            'methods':'GET',   
            // mode: 'cors',
            headers : {
              'Content-Type':'application/json',
            //   "Access-Control-Allow-Methods": "GET, POST, OPTIONS, PUT",
            //   "Access-Control-Allow-Origin": "*",
            //   "Access-Control-Allow-Credentials": "true",
            //   "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
            }
          }) 
        //   .then(response => console.log(response.json()))
          .then(response => response.json())
          .then(response => setArticles(response))
          .catch(error => console.log(error))
      },[]);

//       const search = useLocation().search;
// const id=new URLSearchParams(search).get("id");


    //   const [searchParams, setSearchParams] = useSearchParams();
    //   let meetid=searchParams.get("id")
    //   console.log(meetid)
    const { id } = useParams();

    // console.log("dkj first",props.match.params.mid);
    console.log(id);
return(
    <div className="m-2">
    {/* Display the article details if article is not None */
    console.log(articles,"   from meetupid    ")} 
       {
            <div >
            <h2 className="text-primary"> {articles.Title} </h2>
           
            <p> { articles.description } </p>
            <hr/>
          </div>
        }
    </div>
)

}

export default Meetupid;