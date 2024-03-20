import React from "react";
import ModuleStyle from "../ModuleStyle.module.css";
import Sort from "../Components/categori/Sort";
import Inventory from "../Components/categori/Inventory";

function Categori() {
    return(
    <div className={ModuleStyle.CategoriPage}>
        <Sort/>
        <Inventory/>
    </div>
    )
  }

  export default Categori;