import React from "react";
import styled from 'styled-components';
import CommentDetail from "../model/CommentDetail";

const CommentWord = styled.div`
    font-family: Inter;
    font-weight: bold;
    font-size: 2vw;
    margin-left: 5vw;
`
const Line = styled.hr`
    margin-top: 1.5vw;
    border-width: 4px;
    width: 90%;
    border-color: #000;
`
const CommentPlace = styled.div`
    height: auto;
    width: 90vw;
    padding: 3vw;
`
const CommentBox = styled.div`
    height: 100%;
    width: 100%;
    padding: 1vw;
    border-radius: 10px;
    border: 2px solid #000;
    display: flex;
`
const CommentProfile = styled.img`
    height: 6vh;
    width: 6vh;
`

function Comment() {
    return (
        <>
            <CommentWord>COMMENT</CommentWord>
            <Line/>
            <CommentPlace>
                <CommentBox>
                    <CommentProfile src="https://projectmanager4.s3.ap-northeast-2.amazonaws.com/user+1.svg" alt="로고"/>
                    <CommentDetail></CommentDetail>
                </CommentBox>
            </CommentPlace>
        </>
    );
}

export default Comment;