import React from "react";
import styled from 'styled-components';

const Modledelivery = styled.div`
    height: 40vh; 
    width: 90vw; 
    padding: 3vw;
`

const Modledeliverybox = styled.div`
    height: 100%; 
    width: 100%;
    padding: 2vw;
    border-radius: 10px; 
    border: 2px solid #000;
`

function Modeldrive() {
    return(
        <>
            <Modledelivery>
                <Modledeliverybox>
                    대충 배송비
                </Modledeliverybox>
            </Modledelivery>
        </>
    );
}

export default Modeldrive;