import React from "react";
import "./App.css";
import Topbar from "./Components/Topbar"
import {RecoilRoot} from 'recoil';
import {BrowserRouter as Router, Routes, Route, Navigate, useLocation, BrowserRouter} from 'react-router-dom';
import Main_detail from "./Components/Main_detail";
import Login from "./Components/Login";
import Footer from "./Components/Footer";
import Model_detail from "./Components/Model_detail";

function App() {
  return (
    <>
      <Topbar/>
          <BrowserRouter>
              <Routes>
                  <Route path="/main" element={<Main_detail/>}/>
                  <Route path="/login" element={<Login/>}/>
                  <Route path="/categori" element={<Categori/>}/>
                  <Route path="/model" element={<Model_detail/>}/>
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
