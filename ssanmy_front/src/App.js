import React from "react";
import "./App.css";
import {RecoilRoot} from 'recoil';
import {BrowserRouter as Router, Routes, Route, Navigate, useLocation, BrowserRouter} from 'react-router-dom';
import Main_detail from "./Components/Main_detail";
import Login from "./Components/Login";
import Topbar from "./Pages/Topbar";
import Categori from "./Pages/Categori";

function App() {
  return (
    <>
      <Topbar/>
          <BrowserRouter>
              <Routes>
                  <Route path="/main" element={<Main_detail/>}/>
                  <Route path="/login" element={<Login/>}/>
                  <Route path="/categori" element={<Categori/>}/>
              </Routes>
          </BrowserRouter>
      </>
  );
}

// function AppContent() {
//   return (
//
//   );
// }

export default App;
