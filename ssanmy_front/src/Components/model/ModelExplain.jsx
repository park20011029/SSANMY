import React from "react";
import styled from 'styled-components';
import ModuleStyle from "../../ModuleStyle.module.css";


const ModelInfo = styled.div `
    height: 40vh;
    width: 53vw;
    padding: 3vw;
`
const ModelInfoBox = styled.div`
    background: #D9D9D9;
    padding: 2vw;
    height: 100%;
    width: 100%;
`
const ModelImg = styled.img`
    height: 40vh;
    width: 40vh;
`

function ModelExplain() {
    return(
        <div className={ModuleStyle.Model_explain}>
            <ModelImg src="//thumbnail10.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/1742738348078382-1202e905-701f-4e63-b94c-897babcc7464.jpg"/>
            <ModelInfo>
                <ModelInfoBox>대충 설명</ModelInfoBox>
            </ModelInfo>
        </div>
    );
}

export default ModelExplain;