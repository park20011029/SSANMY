import React from "react";
import styled from 'styled-components';

const Exmodel = styled.div`
  width: 80vw;
  margin: auto; 
  padding-top: 5vh; 
  padding-bottom: 5vh;
  display: flex;
  justify-content: space-around;
`

const ExmodelBox = styled.div`
  width: 15vw;
  height: 15vw;
  background: #D9D9D9;
  border-radius: 2vw;
`

function Com_models() {
    return (
      <>
        <Exmodel>
          <ExmodelBox></ExmodelBox>
          <ExmodelBox></ExmodelBox>
          <ExmodelBox></ExmodelBox>
          <ExmodelBox></ExmodelBox>
          <ExmodelBox></ExmodelBox>
        </Exmodel>
      </>
    );
  }
  
  export default Com_models;