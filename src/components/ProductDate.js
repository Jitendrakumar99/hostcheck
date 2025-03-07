import React from 'react';
import './ProductDate.css';

const ProductDate=(props)=>
{
	const month=props.date.toLocaleString('en-US',{month:'long'});
	const day=props.date.toLocaleString('en-US',{day:'2-degit'});
	const year=props.date.getFullYear();
	return(
		<div className='product-date'>
         <div className='date-font'>{month}</div>
         <div className='date-font'>{year}</div>
         <div className='date-font'>{day}</div>
		</div>
	);
};
export default ProductDate;