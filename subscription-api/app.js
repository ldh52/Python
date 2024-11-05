import express from "express";
import subscriptions from "./data/mock.js";

const app = express();

app.get("/subscriptions", (req, res) => {
  /** 쿼리 파라미터
   *  - sort: 'price'인 경우 높은 요금순, 그 외의 모든 경우 최신으로 생성된 순서
   */
  const sort = req.query.sort;

  const compareFn =
    sort === "price"
      ? (a, b) => b.price - a.price
      : (a, b) => b.createdAt - a.createdAt;

  res.send(subscriptions.sort(compareFn));
});

app.get("/subscriptions/:id", (req, res) => {
  const id = Number(req.params.id);
  const subscription = subscriptions.find((sub) => sub.id === id);
  if (subscription) {
    res.send(subscription);
  } else {
    res.status(404).send({ message: "Cannot find given id." });
  }
});

app.listen(3000, () => console.log("Server Started"));
