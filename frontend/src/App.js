import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";
import './App.css';
import Header from './components/Header';
import StocksListPage from './pages/StocksListPage';

function App() {
  return (
    <Router>
      <div className="App">
        <Header/>
        <Routes>
          <Route path="/" exact element={<StocksListPage/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
