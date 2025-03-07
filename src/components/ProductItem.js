import React from 'react';
import ProductDate from './ProductDate';

import Card from './Card';
import './ProductItem.css'

const ProductItem =(props)=>  
{
	return(
		<Card className="productitem">
			<ProductDate date={props.date}/>
			<div className='productdesc'>
				<h2>
					{props.title}
				</h2>

			</div>

		</Card>
	);
}

export default ProductItem;