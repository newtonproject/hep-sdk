<?php


namespace HepRestApi\Scenarios;


class Order
{
    public $order_number;
    public $price_currency;
    public $total_price;
    public $seller;
    public $customer;
    public $broker;
    public $description;
    public $chain_txid;
    public $order_items = [];

    public function __construct(
        $order_number, # The order number
        $description, # The order description
        $total_price, # The total price of the order.
        $price_currency, # The symbol of fiat or digital token, such as USD, RMB, NEW,BTC,ETH.
        $seller, # The seller's NewID
        $customer, # The customer's NewID
        $broker = '', # The broker's NewID. optional.
        $chain_txid = '' # The txid of blockchain. optional.
    )
    {
        $this->order_number   = $order_number;
        $this->price_currency = $price_currency;
        $this->total_price    = $total_price;
        $this->seller         = $seller;
        $this->customer       = $customer;
        $this->broker         = $broker;
        $this->description    = $description;
        $this->chain_txid     = $chain_txid;
        $this->order_items    = [];
    }

    public function add_order_item(
        $order_item_number, # The identifier of the order item.
        $order_item_quantity, # The number of the item ordered. If the property is not set, assume the quantity is one.
        $price, # The order item's price
        $price_currency, # The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH.
        $thing_name, # The thing name such as product or service name.
        $thing_id, # The thing id such as sku, ISBN.
        $thing_type = 'product' # The thing type such as product or service.
    )
    {
        $this->order_items[] = [
            'order_item_number'   => $order_item_number,
            'order_item_quantity' => $order_item_quantity,
            'price'               => $price,
            'price_currency'      => $price_currency,
            'ordered_item'        => [
                'name'       => $thing_name,
                'thing_id'   => $thing_id,
                'thing_type' => $thing_type,
            ]
        ];
    }

    public function to_dict()
    {
        return [
            'order_number'   => $this->order_number,
            'price_currency' => $this->price_currency,
            'total_price'    => $this->total_price,
            'seller'         => $this->seller,
            'customer'       => $this->customer,
            'broker'         => $this->broker,
            'description'    => $this->description,
            'chain_txid'     => $this->chain_txid,
            'order_items'    => $this->order_items
        ];
    }
}