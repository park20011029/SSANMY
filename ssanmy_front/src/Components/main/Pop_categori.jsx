import React from "react";
import styled from 'styled-components';

const Pcategorititle = styled.div`
    font-family: Inter;
    font-size: 2em;
    color: #000;
    padding-top: 6vh;
    padding-left: 5vw;
`;

const Pcategori = styled.div`
    height: 25vh;
    width: 80vw;
    margin: 5vh 5vw 5vh 5vw;
    display: flex; 
    justify-content: space-around;
`

const CategoriBox = styled.div`
    width: 14vw;
    display: flex;
    flex-direction: column; 
    justify-content: space-between; 
    align-items: center;
`

const CategoriCircle = styled.div`
    width: 10vw;
    height: 10vw; 
    border-radius: 50%; 
    background: #E7E8EA;
`

const CategoriName =styled.div`
    color: #000; 
    font-family: Inter; 
    font-size: 1.5vw; 
    font-style: normal;
    line-height: normal; 
    text-align: center;
`

function Pop_categori() {
    return (
        <>
            <Pcategorititle>인기 카테고리</Pcategorititle>
            <Pcategori>
                <CategoriBox>
                    <CategoriCircle></CategoriCircle>
                    <CategoriName>박민기</CategoriName>
                </CategoriBox>
                <CategoriBox>
                    <CategoriCircle></CategoriCircle>
                    <CategoriName>박민기</CategoriName>
                </CategoriBox>
                <CategoriBox>
                    <CategoriCircle></CategoriCircle>
                    <CategoriName>박민기</CategoriName>
                </CategoriBox>
                <CategoriBox>
                    <CategoriCircle></CategoriCircle>
                    <CategoriName>박민기</CategoriName>
                </CategoriBox>
                <CategoriBox>
                    <CategoriCircle></CategoriCircle>
                    <CategoriName>박민기</CategoriName>
                </CategoriBox>
            </Pcategori>
        </>
    );
  }
  
  export default Pop_categori;