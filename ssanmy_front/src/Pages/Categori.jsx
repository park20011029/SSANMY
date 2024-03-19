import React from "react";
import ModuleStyle from "../ModuleStyle.module.css";
import Sort from "../Components/categori/Sort";

function Categori() {
    return(
    <div className={ModuleStyle.CategoriPage}>
        <Sort/>
    </div>
    )
  }

  export default Categori;