import React from "react";
import ModuleStyle from "../ModuleStyle.module.css";
import Modeldetail from "../Components/model/Modeldetail";
import Modeldrive from "../Components/model/Modeldrive";
import Comment from "../Components/model/Comment";


function Main_detail() {
    return (
        <div className={ModuleStyle.ModelPage}>
            <Modeldetail/>
            <Modeldrive/>
            <Comment/>
        </div>
    )
}

export default Main_detail;