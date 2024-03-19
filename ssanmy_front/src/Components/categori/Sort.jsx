import React from "react";
import styled from 'styled-components';

const CategoriTitle = styled.div`
    font-family: Inter;
    font-size: 2em;
    color: #000;
    padding-top: 6vh;
    padding-left: 5vw;
`;

const Sorted = styled.div`
    display: flex;
`;
const BaseStyle = styled.div`
    height: 3vh;
    margin-left: 5vh;
    border-radius: 20vh;
    background: rgba(217, 217, 217, 0.50);
    text-align: center;
`;

const SortStyle1 = styled(BaseStyle)`
    width: 5vw;
`;

const SortStyle2 = styled(BaseStyle)`
    width: 6vw;
`;

function Sort() {
  return (
    <>
      <CategoriTitle>내가 선택한 카테고리</CategoriTitle>
      <hr />
      <Sorted>
        <SortStyle1>최신</SortStyle1>
        <SortStyle1>가격</SortStyle1>
        <SortStyle2>핫딜값</SortStyle2>
      </Sorted>
      <hr />
    </>
  );
}

export default Sort;
