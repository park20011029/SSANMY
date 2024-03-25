import React from "react";
import ModuleStyle from "../ModuleStyle.module.css";
import Pop_categori from "../Components/main/Pop_categori";
import Com_models from "../Components/main/Com_models";


function Main_detail() {
    return (
        <div className={ModuleStyle.MainPage}>
            <Pop_categori/>
            <Com_models/>
        </div>
    )
}

export default Main_detail;