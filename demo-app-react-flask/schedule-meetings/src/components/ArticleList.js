
const ArticleList = (props) => {
//    let articles = Array.from(props.data);
    return (
        <div className="m-2">
        {/* Display the article details if article is not None */
        console.log(props.articles,"   from article    ")} 
   	    {
                <div >
                <h2 className="text-primary"> { props.articles.Title} </h2>
               
                <p> { props.articles.description } </p>
    	        <hr/>
              </div>
            }
        </div>
        )
}

export default ArticleList;


// const ArticleList = (props) => {

//     return (
//         <div className="m-2">
//         {/* Display the article details if article is not None */
//          console.log(props.articles,"   from article    ")} 
//    	    {props.articles && props.articles.map(article =>{
//             return (

//               <div key= {article.id}>
//                 <h2 className="text-primary"> { article.title} </h2>
                
//                 <p> { article.description } </p>
//     	        <hr/>
//               </div>
//             )
            
//             })}
//         </div>
//         )
// }

// export default ArticleList;