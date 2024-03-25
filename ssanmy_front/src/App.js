import React from "react";
import "./App.css";
import {RecoilRoot} from 'recoil';
import {BrowserRouter as Router, Routes, Route, Navigate, useLocation, BrowserRouter} from 'react-router-dom';
import Main from "./Pages/Main";
import Login from "./Components/Login";
import Topbar from "./Pages/Topbar";
import Categori from "./Pages/Categori";
import Footer from "./Components/Footer";
import Model from "./Pages/Model";

function App() {
  return (
    <>
      <Topbar/>
          <BrowserRouter>
              <Routes>
                  <Route path="/main" element={<Main/>}/>
                  <Route path="/login" element={<Login/>}/>
                  <Route path="/categori" element={<Categori/>}/>
                  <Route path="/model" element={<Model/>}/>
              </Routes>
          </BrowserRouter>
      <Footer/>
      </>
  );
}

// function AppContent() {
//   return (
//
//   );
// }

export default App;
