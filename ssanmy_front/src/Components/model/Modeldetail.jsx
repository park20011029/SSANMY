import React from "react";
import styled from 'styled-components';
import ModelExplain from "../model/ModelExplain";


const ModelName = styled.div`
    font-family: Inter;
    font-size: 3vw;
    margin-left: 5vw;
`


function Modeldetail() {
    return (
        <>
            <ModelName>대충 상품명</ModelName>
            <ModelExplain></ModelExplain>
        </>
    );
}

export default Modeldetail;