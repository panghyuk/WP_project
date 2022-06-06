/* index.html */

const youtubeOne = 'https://www.youtube.com/embed/Hg1gC8bq-6o';
const youtubeTwo = 'https://www.youtube.com/embed/k9S7Tx-GSmQ';
const youtubeThree = 'https://www.youtube.com/embed/I5BfKqOkp1Y';
const youtubeFour = 'https://www.youtube.com/embed/JXFsfqeTLIA';
const youtubeFive = 'https://www.youtube.com/embed/Cw9OIlrNIww';
const youtubeSix = 'https://www.youtube.com/embed/f_SW6i5G7Gk';
const youtubeSeven = 'https://www.youtube.com/embed/mvM69ilcxas';
const youtubeEight = 'https://www.youtube.com/embed/0TF2ZFpSpxo';
const youtubeNine = 'https://www.youtube.com/embed/cj7_pgUrtWE';

const contentIssueFirst = document.querySelector("#content_issue_first");
const contentIssueSecond = document.querySelector("#content_issue_second");
const contentIssueThird = document.querySelector("#content_issue_third");
const controls = document.querySelector(".controls");
const prevButton = document.querySelector(".prev");
const presentButton = document.querySelector(".present");
const nextButton = document.querySelector(".next");
const contentIssueFirstClass = document.querySelector(".content_issue_first");
const contentIssueFirstClassIframes = contentIssueFirstClass.querySelectorAll("iframe");
function clearFirstSrc(){
    for(i = 0; i < contentIssueFirstClassIframes.length; i++){
        contentIssueFirstClassIframes[i].src = "";
    }
}

let totalPages = 3;
let currentPage = 1;


function clearCheckPage(){
    prevButton.style.visibility = "visible";
    nextButton.style.visibility = "visible";
    contentIssueFirst.style.display = "none";
    contentIssueSecond.style.display = "none";
    contentIssueThird.style.display = "none";
}

function checkPage(){
    clearCheckPage();
    clearFirstSrc();
    
    let contentIframes = "";
    switch(currentPage){
        case 1:
            contentIframes = contentIssueFirst.querySelectorAll("#content_issue_video_iframe");
            contentIframes[0].src = youtubeOne;
            contentIframes[1].src = youtubeTwo;
            contentIframes[2].src = youtubeThree;
            prevButton.style.visibility = "hidden";
            contentIssueFirst.style.display = "flex";
            break;
        case 2:
            contentIframes = contentIssueSecond.querySelectorAll("#content_issue_video_iframe");
            contentIframes[0].src = youtubeFour;
            contentIframes[1].src = youtubeFive;
            contentIframes[2].src = youtubeSix;
            contentIssueSecond.style.display = "flex";
            break;
        case 3:
            contentIframes = contentIssueThird.querySelectorAll("#content_issue_video_iframe");
            contentIframes[0].src = youtubeSeven;
            contentIframes[1].src = youtubeEight;
            contentIframes[2].src = youtubeNine;
            nextButton.style.visibility = "hidden";
            contentIssueThird.style.display = "flex";
            break;
    }
}

function goPrev(){
    currentPage -= 1;
    presentButton.innerText = ` ${currentPage} / ${totalPages} `
    checkPage();
}
function goNext(){
    currentPage += 1;
    presentButton.innerText = ` ${currentPage} / ${totalPages} `
    checkPage();
}
