import express from 'express';
import subscriptions from './data/mock.js';

const app = express();
app.use(express.json());

app.get('/subscriptions', (req, res) => {
  /** 쿼리 파라미터
     *  - sort: 'price'인 경우 높은 요금순, 그 외의 모든 경우 최신으로 생성된 순서
     */
  const sort = req.query.sort;

  const compareFn =
    sort === 'price'
      ? (a, b) => b.price - a.price
      : (a, b) => b.createdAt - a.createdAt;

  res.send(subscriptions.sort(compareFn));
});

app.get('/subscriptions/:id', (req, res) => {
  const id = Number(req.params.id);
  const subscription = subscriptions.find((sub) => sub.id === id);
  if (subscription) {
    res.send(subscription);
  } else {
    res.status(404).send({ message: 'Cannot find given id.' });
  }
});

function getNextId(arr) {
  const ids = arr.map((elt) => elt.id);
  return Math.max(...ids) + 1;
}

app.post('/subscriptions', (req, res) => {
  const newSubscription = req.body;
  newSubscription.id = getNextId(subscriptions);
  newSubscription.createdAt = new Date();
  newSubscription.updatedAt = new Date();
  subscriptions.push(newSubscription);
  res.status(201).send(newSubscription);
});

app.listen(3000, () => console.log('Server Started'));
