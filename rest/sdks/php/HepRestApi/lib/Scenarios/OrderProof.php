<?php


namespace HepRestApi\Scenarios;


class OrderProof
{
    public $price_currency;
    public $total_price;
    public $submitter;
    public $proof_type;
    public $orders;

    public function __construct(
        $total_price, # The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.
        $price_currency, # The symbol of fiat or digital token, such as USD, RMB, NEW,BTC,ETH.
        $submitter, # The submitter's NewID
        $proof_type = 'order' # The proof type which value is "order".
    )
    {
        $this->price_currency = $price_currency;
        $this->total_price    = $total_price;
        $this->submitter      = $submitter;
        $this->proof_type     = $proof_type;
        $this->orders         = [];
    }

    public function add_order($order)
    {
        $this->orders[] = $order;
    }

    public function to_dict()
    {
        return [
            'price_currency' => $this->price_currency,
            'total_price'    => $this->total_price,
            'submitter'      => $this->submitter,
            'proof_type'     => $this->proof_type,
            'orders'         => $this->orders
        ];
    }
}