import logo from './logo.svg';
import './App.css';
import {useState,useEffect} from 'react';
import { Queries } from './Components/Deploy/Queries';
import {Test} from './Components/Test'
import { Table,Column,HeaderCell,Cell,Pagination } from 'rsuite-table';
import 'rsuite-table/lib/less/index.less';
import "rsuite/dist/rsuite.min.css";


function App() {
  const [query,setQuery] = useState([]);

  useEffect(() => {
    fetch('/values').then(response => 
      response.json().then(data => {
        setQuery(data);
      }))
  }, [])
  
          /*<Queries queries={query}/> */

  return (
    <div >
        <Table
          
          bordered
          cellBordered
          virtualized
          height={700}
          data={query}
          onRowClick={data => {
            console.log(data);
          }}
        >
          <Column width={70} align="center" fixed>
            <HeaderCell>Id</HeaderCell>
            <Cell dataKey="id" />
          </Column>

          <Column width={160}>
            <HeaderCell>Date</HeaderCell>
            <Cell dataKey="date" />
          </Column>

          <Column width={160}>
            <HeaderCell>Item</HeaderCell>
            <Cell dataKey="item" />
          </Column>

          <Column  width={200}>
            <HeaderCell>Value</HeaderCell>
            <Cell dataKey="value" />
          </Column>
          
          
        </Table>

        
    </div>
  );
}

export default App;
