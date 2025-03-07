import "./Card.css";
const Card = (props) => {
  const classes = "card" + props.className;
  console.log(classes)
  return <div className={classes}>{props.childern}</div>;
};
export default Card;
