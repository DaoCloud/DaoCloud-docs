import * as dotenv from "dotenv";
import { OpenAI } from "langchain";
import { OpenAIEmbeddings } from "langchain/embeddings";
import { TextLoader, DirectoryLoader } from "langchain/document_loaders";
import { MarkdownTextSplitter } from "langchain/text_splitter";
// import { loadQAMapReduceChain } from "langchain/chains";
import { SupabaseVectorStore } from "langchain/vectorstores";
// import { SupabaseLibArgs } from "langchain/vectorstores_supabase";
import { createClient } from "@supabase/supabase-js";
import { json2csv } from "json-2-csv"
import fs from "fs"
import path from "path"

dotenv.config();

// const model = new OpenAI({ temperature: 0, maxConcurrency: 10 });
// from langchain.document_loaders import DirectoryLoader


function loaderDocs(type: String = "Dir") {

  if (type == "file") {
    // 单文件
    const loader = new TextLoader("src/data/index.md");
    return loader.load();
  }

  // if (type == "Dir") {
  // 目录
  const loader = new DirectoryLoader("../../../docs/zh/docs/", {
    ".md": (path) => new TextLoader(path),
  });

  // return;
  return loader.load();
  // }

}

const docs = await loaderDocs();
// console.log({ docs });

const splitter = new MarkdownTextSplitter({
  chunkSize: 3000,
  chunkOverlap: 100,
});
const output = await splitter.splitDocuments(docs);


const format = output.map((item, i) => {


  const relativeFilePath = path.relative('/Users/yeting/project/DaoCloud-docs/docs/zh/docs',
    item.metadata['source']); // 根据实际项目文件结构进行调整
  const relativeDirPath = path.dirname(relativeFilePath); // 根据实际项目文件结构进行调整

  // const relativeDirPath = path.relative('/Users/yeting/project/DaoCloud-docs/docs/zh/docs',
  //   path.dirname(item.metadata['source'])); // 根据实际项目文件结构进行调整
  // 对应文档站的路径
  const htmlReplacementPath = `https://docs.daocloud.io/${relativeFilePath.replace("md", "html")}`;
  // 图片的基础路径
  const imageReplacementPath = `https://docs.daocloud.io/${relativeDirPath}`;

  // console.log("==========", htmlReplacementPath, imageReplacementPath)

  // console.log(item.metadata['source'], imageReplacementPath)

  // 替换图片路径
  const replacedImagePath = item.pageContent.replace(/(\.\.\/)+images/g, (matchedPath) => {
    return `${imageReplacementPath}/${matchedPath}`;
  });

  // 替换 .md 路径
  const replacedMdPath = replacedImagePath.replace(/\.\.\/\.\.\/(.+?)\.md/g, "https://docs.daocloud.io/$1");


  const fastQA = {
    question: replacedMdPath,
    // answer: '',
    answer: htmlReplacementPath
    // source: replacementPath

  }
  // console.log(relativePath)
  // console.log(replacedMdPath.length, item.pageContent.length,htmlReplacementPath)
  // if (replacedMdPath.length < 50) {

  //   // console.log(output[i ? i - 1 : i]['pageContent'])
  //   // console.log(replacedMdPath.length, replacedMdPath)
  //   // console.log(output[i + 1]['pageContent'])
  // }
  return fastQA
})
const csv = json2csv(format)

csv.then(res => {

  // console.log(res)

  // 将处理后的数据写入新的文件
  fs.writeFile('output.csv', res, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('CSV 文件已保存为 output.csv');
  });
})

// Supabase
// const privateKey = process.env.SUPABASE_PRIVATE_KEY;
// if (!privateKey) throw new Error(`Expected env var SUPABASE_PRIVATE_KEY`);

// const url = process.env.SUPABASE_URL;
// if (!url) throw new Error(`Expected env var SUPABASE_URL`);

// const client = createClient(url, privateKey);

// const vectorStore = await SupabaseVectorStore.fromDocuments(output, new OpenAIEmbeddings(), {
//   client,
//   tableName: "documents",
//   queryName: "match_documents",
// })

// console.log(output)

// const chain = loadQAMapReduceChain(model);


// const res = await chain.call({
//   input_documents: output,
//   question: "DCE 是什么",
// });

// console.log(output);
// console.log({ res });


// console.log(docs);




// const model = new OpenAI({
//   modelName: "gpt-3.5-turbo",
//   openAIApiKey: process.env.OPENAI_API_KEY,
// });

// const res = await model.call(
//   "What's a good idea for an application to build with GPT-3?"
// );


// 写入文件

