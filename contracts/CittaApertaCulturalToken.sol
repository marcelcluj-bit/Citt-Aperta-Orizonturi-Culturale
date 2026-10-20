// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CittaApertaCulturalToken
 * @dev Smart Contract pentru Tokenizarea Patrimoniului Cultural și Redevențelor în cadrul Proiectului Città Aperta
 */
contract CittaApertaCulturalToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18; // 1 Milion tokenuri CACT

    // Eveniment pentru urmărirea distribuției redevențelor culturale
    event RoyaltiesDistributed(address indexed beneficiary, uint256 amount);

    constructor() ERC20("Citta Aperta Cultural Token", "CACT") Ownable(msg.sender) {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Distribuie redevențe sau dividende din vânzările de artă / turism către beneficiari
     */
    function distributeRoyalties(address beneficiary, uint256 amount) external onlyOwner {
        require(balanceOf(msg.sender) >= amount, "Fonduri insuficiente pentru distribuirea redeventelor");
        _transfer(msg.sender, beneficiary, amount);
        emit RoyaltiesDistributed(beneficiary, amount);
    }
}
