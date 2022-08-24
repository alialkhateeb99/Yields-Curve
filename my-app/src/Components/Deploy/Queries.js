import React from 'react';


export const Queries = ({ queries }) => {
    return(
        
        <div> 
            {queries.map(query => {
                return (
                    <div> {query.date}  {query.value}</div>
                )
            })}
        </div>
    )
}